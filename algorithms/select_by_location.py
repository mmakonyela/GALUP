import sys
import os
from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterDistance,
                       QgsProcessingParameterEnum)
from pylusat import geotools


class SelectByLocation(QgsProcessingAlgorithm):
    INPUT = "INPUT"
    SELECT = "SELECT"
    OP = "OP"
    DIST = "DIST"
    OUTPUT = "OUTPUT"

    def tr(self, string, context=''):
        if context == '':
            context = self.__class__.__name__
        return QCoreApplication.translate(context, string)

    def group(self):
        return self.tr("LUCIS-OPEN Tools for QGIS")

    def groupId(self):
        return "lucisopen"

    def __init__(self):
        super().__init__()
        self.op_option = (
            ('Intersects', self.tr('Intersects')),
            ('Contains', self.tr('Contains')),
            ('Within', self.tr('Within')),
            ('Within a distance', self.tr('Within a distance'))
        )

    def name(self):
        return "selectbylocation"

    def displayName(self):
        return self.tr("Select by Location")

    def shortHelpString(self):
        return self.tr("Select part of the input Layer based on its "
                       "relationship with the selecting layer.")

    def createInstance(self):
        return SelectByLocation()

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                types=[QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.SELECT,
                self.tr('Selection layer'),
                types=[QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterEnum(
                self.OP,
                self.tr('Join option (geometric predicate)'),
                options=[o[1] for o in self.op_option],
                defaultValue=0
            )
        )
        within_dist = QgsProcessingParameterDistance(
            self.DIST,
            self.tr('Within distance of selecting feature'),
            parentParameterName=self.SELECT
        )
        within_dist.setMetadata({
            'widget_wrapper': {
                'decimals': 3
            }
        })
        self.addParameter(within_dist)
        self.addParameter(
            QgsProcessingParameterVectorDestination(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        input_lyr = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        select_lyr = self.parameterAsVectorLayer(parameters, self.SELECT, context)
        op = self.op_option[self.parameterAsEnum(parameters, self.OP,
                                                 context)][0].lower()
        within_dist = self.parameterAsDouble(parameters, self.DIST, context)
        output_file = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)

        sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
        from loqlib import LUCISOpenQGISUtils

        input_gdf = LUCISOpenQGISUtils.vector_to_gdf(input_lyr)
        select_gdf = LUCISOpenQGISUtils.vector_to_gdf(select_lyr)
        output = geotools.select_by_location(input_gdf, select_gdf,
                                             op, within_dist)
        if not output.empty:
            output.to_file(output_file)
            return {self.OUTPUT: output_file}
        else:
            feedback.pushInfo('No features in input layer met the specified '
                              'spatial relationship. No output generated.')

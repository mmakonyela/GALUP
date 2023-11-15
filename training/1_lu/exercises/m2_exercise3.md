# Module 2 - Exercise 3

## 1. Skills Practices

This exercise will practice:

- [Reclassify Field](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#23-reclassify-field)
- [Zonal Statistics](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#25-zonal-statistics)

## 2. Description

Sorghum is an important staple food crop in Botswana and is produced throughout the
country, though the production does not meet the demand. In the Chobe district, the Pandamatenga farmers wants to
plan and develop new cropland to grow sorghum.
Therefore, as planners, we need to evaluate the suitability of land for
growing sorghum in the Pandamatenga landscape.

The first step of our analysis aims to select out the area with a suitable
soil clay content. Clays are the source of many of the chemical and physical properties of soils that make them a useful medium for the growth of plants and for the less common uses such as a medium for the disposal of wastes. Heavy soils produce the best yields in good seasons, but during times of stress sandier soils are better; however, during a normal drought grain sorghum will still produce satisfactory yields on soils with a clay content of more than 50%, whereas other crops like maize will yield very little grain.


So, we will evaluate the land in Pandamatenga landscape by analyzing the clay content dataset in depth ranged from 0 to 20 cm.

In this exercise, we will create a clay content index to evaluate the suitability
to grow sorghum in the Pandamatenga landscape by using the [Reclassify Field](https://github.com/mogaetkpp/GALUP/blob/master/training/1_lu/modules/module2.md#23-reclassify-field) tool and [Zonal Statistics](https://github.com/mogaetkpp/GALUP/blob/master/training/1_lu/modules/module2.md#25-zonal-statistics) tool.

## 3. GIS Dataset

You should use the following data to finish this exercise:
- _ClayContent.tif_ at
`GALUP-master -> training -> 1_lu -> datasets -> Pandamatenga Clay Content`
- _PND_IDUs.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Pandamatenga Landscape IDUs`
## 4. Instruction

1. Locate _ClayContent.tif_ and _PND_IDUs.shp_ in the **_Browser Panel_** and add them to **_Map Canvas_**.
2. In the **_Processing Toolbox_** panel, locate the
   **<ins>Zonal Statistics</ins>** tool under **_PyLUSATQ_**
<img src="https://github.com/mogaetkpp/GALUP/blob/master/img/gui/icon/PyLUSATQ.svg" alt= "scripts" width="20"> plugin.
3. **Double Click** to open the tool and set parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: PND_IDUs,</li>
      <li><b>Raster layer</b>: ClayContent,</li>
      <li><b>Types of statistics</b>: mean,</li>
      <li><b>Output column prefix</b>: Clay_Cont,</li>
      <li><b>Output layer</b>: ClayCont.shp,</li>
      <li>leave all other parameters as default.</li>
   </ol>
4. Click **Run**.
5. Open **<ins>Reclassify Field</ins>** tool under **_PyLUSATQ_**
<img src="https://github.com/mogaetkpp/GALUP/blob/master/img/gui/icon/PyLUSATQ.svg" alt= "scripts" width="20"> plugin.
6. **Double Click** to open the tool and set parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: ClayCont,</li>
      <li><b>Field to reclassify</b>: Clay_Cont_mean,</li>
      <li><b>Old values</b>: 6.4-10.5, 10.5-13.1, 13.1-33.5, 33.5-38.5, 38.5-60.1,</li>
      <li><b>New values</b>: 1, 2, 3, 4, 5, </li>
      <li><b>Output column name</b>: ClayReclas,</li>
      <li><b>Output layer</b>: Reclassed_ClayContent.shp,</li>
      <li>leave all other parameters as default.</li>
   </ol>
7. Click **Run**.
8. Now let's setup the **Symbology** of the output layer (_Reclassed\_ClayContent.shp_).
   Open the
   <img src="../../../img/gui/icon/symbology.svg" alt= "AttrTbl" width="20">
   Symbology tab from the **_Layer Properties_** window.
   Select the ![categorized](../../../img/gui/icon/rendererCategorizedSymbol.svg)
   Categorized style.
   Specify the _ClayReclas_ field as **Value**, then choose the _Greens_ color ramp
   with 3 classes. Click **Apply**.
9. Click **OK** on the **Symbology** tab.
10. Create a _Layout_, then add _Legend_, _Scale bar_, and _North Arrow_ to the
   layout.
11. Export the map as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](../pdf_maps/M2E3_ClayCont.pdf).
- Now you have completed all exercises. Please go back to
  [Module 2](https://github.com/mogaetkpp/GALUP/blob/master/training/1_lu/modules/module2.md#7-exercises-and-post-training-survey) to turn in them.

## 6.Reference

1. Pannar Seeds. (2013). Grain Sorghum: Production Guide. https://www.pannar.com/assets/documents/grain_sorghum_op.pdf

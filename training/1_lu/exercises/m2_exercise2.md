# Module 2 - Exercise 2

## 1. Skills Practiced

This exercise will practice:

- [Select by Location](https://github.com/mogaetkpp/GALUP/blob/master/training/1_lu/modules/module2.md#26-select-by-location)

## 2. Description

Normally, the cattle posts will be placed not close to each other to avaid overstocking and overgrazing, but generally due to constraints, they are placed near a water source like borehole so that it will be convenient to water livestock. In this exercise, we will help to find out the IDUs of Pandamatenga landscape that are in proximity (within the 4 kilometers) to a cattlepost by using the [Select by Location](https://github.com/mogaetkpp/GALUP/blob/master/training/1_lu/modules/module2.md#26-select-by-location) tool.

## 3. GIS Dataset

The following datasets are used in this exercises:
- _PND\_IDUs.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Pandamatenga Landscape IDUs`.
- _Cattle\_Posts.shp_ at `GALUP-master -> training -> 1_lu -> datasets -> Cattle Posts Location in Pandamatenga Landscape`.

## 4. Instruction

1. Locate _PND\_IDUs.shp_ and _Cattle\_Posts.shp_ in the
   **_Browser Panel_** and add them to **_Map Canvas_**.
2. In the **_Processing Toolbox_** panel, locate the
   **<ins>Select by Location</ins>** tool under _PyLUSATQ_
<img src="https://github.com/mogaetkpp/GALUP/blob/master/img/gui/icon/PyLUSATQ.svg" alt= "scripts" width="20">.
3. **Double Click** to open the tool and set parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: PND_IDUs,</li>
      <li><b>Selection layer</b>: Cattle_Posts,</li>
      <li><b>Join option</b>: Within a distance,</li>
      <li><b>Within distance of selecting feature</b>: 4 kilometers,</li>
      <li><b>Output layer</b>: <i>CttlProIDU.shp</i>,</li>
      <li>leave all other parameters as default.</li>
   </ol>
4. Click **Run**.
5. Set the symbology for the output polygons (match the color as the pdf file
   below).
6. Create a _Layout_ and then add _Legend_, _Scale bar_, and _North Arrow_.
7. Export the map as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](../pdf_maps/M2E2_SelLoc.pdf).
- Please go back to
  [Module 2](https://github.com/mogaetkpp/GALUP/blob/master/training/1_lu/modules/module2.md#7-exercises-and-post-training-survey) to complete the third exercise.

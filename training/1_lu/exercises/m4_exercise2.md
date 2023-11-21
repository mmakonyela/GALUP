# Module 4 - Exercise 2

## 1. Skills Practiced

This exercise will practice:

- **Analytic Hierarchy Process (AHP)**

## 2. Description

As a planner, you are trying to make land-use decisions for Pandamatenga by using LUCIS.
Now you have identified four agricultural land-use purposes (goals): **Row crops**,
**Livestock**, **Horticulture**, and **Orchards**.
After finishing building up the suitability modeling for each land-use purpose,
you are ready to assign weights to these four purposes by using AHP.
Because these are agricultural land-use purposes, you asked four farmers about
their interests and find:

- The first farmer mainly plants row crops.
- The second farmer focuses on livestock.
- The third farmer does vegetable production.
- The fourth farmer is an owner of orchards.

Four farmers assign land-use suitability weights to each purposes as follows:

![farmers](../../../img/qgm/algtbl/m4_e2_aph_4farmers_1.svg)

Note that their opinions are equally weighted (i.e., 0.25 for each
farmer).

Use the **_Compute AHP Weights_** tool in OPEN-LUCIS to compute the weights
for the four land-use purposes.

> :bulb: Note:<br>
> For fractional inputs, please refer to the [Compute AHP Weights](https://github.com/SERVIR-WA/GALUP/wiki/Tools#compute-ahp-weights) tool instruction.

## 3. Instruction

1. Open the **_Compute AHP Weights_** tool in QGIS.
2. Select **Define AHP weights** for _Weights generating options_.
3. For the _List of criteria to weight_, click the "..." button and double
   click to change the default name "Criteria 1", "Criteria 2", and
   "Criteria 3" to `Row crops`, `Livestock`, and `Horticulture` respectively.
4. Click **Add Row** button to add a new row and name it as
   `Orchards`. Then, click **OK**.
5. For the _Comparison table for creating the reciprocal matrix_, click the
   "..." button and add three new rows by click **Add Row** button. You need to
   fill out the values in each form in this table.
6. Take the form of **Farmer 4** as an example, set the parameters in the
   table as follows:
   <img src="../../../img/gui/window/m4_e2_ahp_setting.png" alt= "AttrTbl" width="600"><br>
   Note that _Row id_ and _Column id_ denote the row index and column index
   in the matrix respectively.
   For instance, _Row id_ 2 and _Column id_ 3 represents the cell in second row
   and third column in the form of **Farmer 4**. the _Pair-wise importance_
   stores the value in that cell, which is 1/2 (0.5).
7. Click **OK** to close the window, and click **Run**.
8. Repeat the process above to calculate the weights for the forms of
   **Farmer 1**, **Farmer 2**, and **Farmer 3**.

## 5.Result

- Follow the steps above, put your result into a spread sheet and turn it in.
- Please go back to [Module 4](https://github.com/mogaetkpp/GALUP/blob/master/training/1_lu/modules/module4.md#5-Exercises) to complete the
  third exercise.

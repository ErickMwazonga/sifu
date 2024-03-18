## 610. Triangle Judgement
https://leetcode.com/problems/triangle-judgement/description/

```
Table: Triangle
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.

Report for every three line segments whether they can form a triangle.
Return the result table in any order.

The result format is in the following example.

Example:
Input:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+

Output:
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+

Intuition
We need to find whether the given three line segments can form a triangle.

Triangle Inequality Theorem
for a triangle to be formed, the sum of the lengths of any two sides must be greater than (or equal to) the length of the third side.
```

### SQL Solution 1
```sql
SELECT x, y, z,
    CASE
        WHEN x + y > z AND x + z > y AND y + z > x
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;
```

### SQL Solution 2
```sql
SELECT x, y, z,
    IF(
        ((x + y) > z AND (y + z) > x AND (x + z) > y), "Yes", "No"
    ) AS triangle
FROM triangle
```

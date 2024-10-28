'''
Task: Design classes for excel spreadsheet and implement following requirements:

1. Excel file contains multiple worksheets.
2. Each worksheet contains rows and columns.
3. Each cell can contain any value. // string/integer/date
4. Spreadsheet should have methods to set and get values

Spreadsheet
    Worksheet
        cells(row, col) -> value
        row
        col
        
    Operations
        set/get
        
    
    Hashmap(key -> (row, col))
    2D array - lookup - O(1)
    
    Space O(N_ROWS)
    -> Hashmap - (Rows * cols)
        rows -> {
            col: value
        }
'''

from collections import defaultdict


class WorkSheet:
    
    def __init__(self):
        self.workseet = defaultdict(dict)
        
    def get_row(self, row: int) -> Row | int:
        return self.worksheet.get(row, -1)
        
    def get_cell(self, row: int, column: int) -> Cell | int:
        if self.get_row(row) == -1:
            return -1
            
        return self.worksheet[row].getCell(column)
        

class Row:
    
    def __init__(self, row: int) -> None:
        self.row = row
        self.columns = {}
        
    def setCell(self, column: int, cell: Cell) -> None:
        self.columns[column] = cell
        
    def getCell(self, column: int) -> Cell | int:
        return self.columns.get(column, -1)
        
        
class Cell: # 5, 5
    
    def __init__(self) -> None:
        self.value = None
        self.ref = Cell | None # 10, 10
        self.ref = [(10, 10), (3, 2), (7, 8)]
        
    def setValue(self, value):
        ...
        
'''
// formula can have reference to another cell
5, 5 -> hello
10, 10 -> 5, 5 -> hello     
'''   


'''
interface ICell {
    String getValue();
    
    void setValue(String value);
}


interface IRow {
    ICell getCell(int column);

    void setCell(int column, ICell cell);
}

/**
 * High-level representation of an Excel workbook. 
 * It is also the top level object for creating new sheets/etc.
 */
interface IWorkBook {
    // just examples of methods, not need to implement all of them
    IWorksheet createSheet(String sheetName);
}

/**
 * High-level representation of an Excel worksheet.
 */
interface IWorksheet {
    IRow getRow(int row);

    ICell getCell(int row, int column);
}

/**
 * High-level representation of a row of a worksheet.
 */



/**
 * High-level representation of a cell in a row of a worksheet.
 */
'''

from collections import defaultdict
from typing import Union, Dict, Tuple, Optional


class Cell:
    def __init__(self, value: Optional[Union[str, int, float]] = None) -> None:
        self.value = value
        self.ref = None  # Reference to another cell

    def set_value(self, value: Union[str, int, float]) -> None:
        self.value = value

    def get_value(self) -> Union[str, int, float, None]:
        return self.value


class Row:
    def __init__(self) -> None:
        self.columns: Dict[int, Cell] = {}

    def set_cell(self, column: int, cell: Cell) -> None:
        self.columns[column] = cell

    def get_cell(self, column: int) -> Union[Cell, None]:
        return self.columns.get(column)


class WorkSheet:
    def __init__(self) -> None:
        self.worksheet: Dict[int, Row] = defaultdict(Row)

    def set_cell(self, row: int, column: int, value: Union[str, int, float]) -> None:
        if row not in self.worksheet:
            self.worksheet[row] = Row()
        if column not in self.worksheet[row].columns:
            self.worksheet[row].set_cell(column, Cell())
        self.worksheet[row].get_cell(column).set_value(value)

    def get_cell(self, row: int, column: int) -> Union[Cell, None]:
        return self.worksheet[row].get_cell(column) if row in self.worksheet else None

    def get_value(self, row: int, column: int) -> Union[str, int, float, None]:
        cell = self.get_cell(row, column)
        return cell.get_value() if cell else None


class Spreadsheet:
    def __init__(self) -> None:
        self.sheets: Dict[str, WorkSheet] = {}

    def add_worksheet(self, name: str) -> None:
        if name not in self.sheets:
            self.sheets[name] = WorkSheet()

    def set_value(self, sheet_name: str, row: int, column: int, value: Union[str, int, float]) -> None:
        if sheet_name in self.sheets:
            self.sheets[sheet_name].set_cell(row, column, value)
        else:
            raise ValueError(f"Worksheet {sheet_name} does not exist.")

    def get_value(self, sheet_name: str, row: int, column: int) -> Union[str, int, float, None]:
        if sheet_name in self.sheets:
            return self.sheets[sheet_name].get_value(row, column)
        else:
            raise ValueError(f"Worksheet {sheet_name} does not exist.")


# Example usage:
spreadsheet = Spreadsheet()
spreadsheet.add_worksheet("Sheet1")
spreadsheet.set_value("Sheet1", 1, 1, "Hello")
spreadsheet.set_value("Sheet1", 1, 2, 123)

print(spreadsheet.get_value("Sheet1", 1, 1))  # Output: Hello
print(spreadsheet.get_value("Sheet1", 1, 2))  # Output: 123
print(spreadsheet.get_value("Sheet1", 2, 1))  # Output: None

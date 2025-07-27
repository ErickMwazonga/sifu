## Data Structures
### ✅ Vector
std::vector is a dynamic array that can resize automatically.

#### 🔸 Syntax
```cpp
vector<Type> vectorName;

// initialize on declaration:
vector<Type> vectorName = {value1, value2, value3};
```

#### 🔹 Examples
```cpp
vector<int> numbers = {1, 2, 3, 4, 5};

numbers.push_back(6); // add an element

// access elements
int first = numbers[0]; 
int last = numbers.back(); 
int front = numbers.front();
int atIndex2 = numbers.at(2);

numbers[1] = 10; // modify elements
```

#### 🔹 Usage
```cpp
vector<int> nums = {10, 20, 30, 40, 50};

// loop through vector elements using range-based for loop
for (int num : nums) {
    cout << num << endl;
}

// loop using index: forward + reverse
for (size_t i = 0; i < nums.size(); i++) {}
for (int i = nums.size() - 1; i >= 0; --i) {}

// loop using iterators: forward + reverse
for (auto it = nums.begin(); it != nums.end(); ++it) {}
for (auto rit = nums.rbegin(); rit != nums.rend(); ++rit) {}
```

### ✅ Pair
std::pair lets you store two related values together.

#### 🔸 Syntax
```
pair<Type1, Type2> pairName;

// initialize on declaration:
pair<Type1, Type2> pairName(value1, value2);
```

#### 🔹 Examples
```cpp
pair<int, int> point(10, 20);  // x = 10, y = 20
    
// modify elements
point.first = 30;
point.second = 40;
```

#### 🔹 Usage
```cpp
vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

for (const pair<int, int>& dir : directions) {
    cout << "x: " << dir.first << ", y: " << dir.second << endl;
}

// using structured bindings to unpack the pair
for (const auto& [x, y] : directions) {
    cout << "x: " << x << ", y: " << y << endl;
}
```

### ✅ Unordered Map  
`std::unordered_map` is a hash table based container that stores key-value pairs with average O(1) lookup, insertion, and deletion.

#### 🔸 Syntax
```cpp
unordered_map<KeyType, ValueType> mapName;

// initialize on declaration:
unordered_map<string, int> mapName = {
    {"apple", 1}, {"banana", 2}, {"orange", 3}
};
```

#### 🔹 Examples
```cpp
unordered_map<string, int> fruitCount = {
    {"apple", 5}, {"banana", 3}
};

// insert or update a key-value pair
fruitCount["orange"] = 7;

// access value by key
int apples = fruitCount["apple"];
int bananas = fruitCount.at("banana");    // throws if key not found

// check if a key exists
bool hasMango = fruitCount.find("mango") != fruitCount.end();
bool hasMango = fruitCount.count("mango") > 0;
bool hasMango = fruitCount.contains("mango"); // C++20 

// remove a key-value pair
fruitCount.erase("banana");
```

## Tricks
### ✅ Inline Variable Declaration
Declare and initialize variables on the same line.

#### 🔸 Syntax
```
type variableName1 = value1, variableName2 = value2;
```
#### 🔹 Examples
```cpp
int a = 10, b = 20;
```

### ✅ Ternary Operator
The ternary operator is a shorthand for `if-else` in C++.
#### 🔸 Syntax

```cpp
condition ? value_if_true : value_if_false;
```
#### 🔹 Examples
```cpp
int a = 10, b = 20;
int maxVal = (a > b) ? a : b;  // maxVal = 20
```

### ✅ Structured Bindings (C++17)
Unpack tuples or pairs into variables cleanly.

#### 🔹 Examples
```cpp
pair<int, string> person = {"Erick", 12};
auto [name, age] = person;
```

### ✅ 7. Swap without temp variable
```cpp
a ^= b;
b ^= a;
a ^= b;

// short-hand
std::swap(a, b);
```
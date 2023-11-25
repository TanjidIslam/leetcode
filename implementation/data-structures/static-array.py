from typing import Any


class StaticArary:
    def __init__(self, size) -> None:
        self.size = size
        self.data = [None] * size
    
    def get(self, index: int) -> Any:
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of bounds")

    def set(self, index: int, value: Any) -> None:
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        tmp = []
        for item in self.data:
            if item is not None:
                tmp.append(str(item))
        return "[" + ", ".join(tmp) + "]"

first_year_courses = StaticArary(int(input("How many courses are you taking in first year?: ")))
for i in range(len(first_year_courses)):
    first_year_courses.set(i, input(f"Enter the name of course #{i+1}: "))
    print("Courses added so far:", first_year_courses)
print("Your courses are:", first_year_courses)
print("The first course is:", first_year_courses.get(0))
print("The last course is:", first_year_courses.get(len(first_year_courses) - 1))
print("Total number of courses:", len(first_year_courses))

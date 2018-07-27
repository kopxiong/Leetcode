# Now given the employee information of a company, and an employee id,
# you need to return the total importance value of this employee and all his subordinates.

# Binary search: Time complexity: O(N); Space complexity: O(N) (call stack)

# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # using hash map, is a dictionary
        hash_map = {e.id: e for e in employees}

        # dfs algorithm, always can use recursion
        def dfs(eid):
            employee = hash_map[eid]
            return employee.importance + sum(dfs(eid) for eid in employee.subordinates)

        return dfs(id)

if __name__ == "__main__":
    employees = [Employee(0, 5, [2, 3]), Employee(2, 6, []), Employee(3, 9, [])]
    id = 0

    print(Solution().getImportance(employees, id))

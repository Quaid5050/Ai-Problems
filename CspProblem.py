# thing we need some for cfc and baktracking
# back tracking()
# backtracking search()
# recursive backtracking search()
# select unassigned variable()
# order domain value()

#CSP(variable, domain,constrain)
# assignvariable()  unassignedvariable()  inconflicconstrainchacking()

# our expected output is...
# initialize csp problem
# {'a': 1, 'b': 2, 'c': 1}

from functools import reduce

class CSP:
    def __init__(self, var, domains, constraints, neighbors):
        print("initialize csp problem")
        self.var = var
        self.domains = domains
        self.constraints = constraints
        self.neighbors = neighbors

    def assign(self, var, val, assignment):
        assignment[var] = val

    def unassign(self, var, assignment):
        if var in assignment:
            del assignment[var]

    def nconflicts(self, var, val, assignment):
        def conflict(var2):
            val2 = assignment.get(var2, None)
            return val2 != None and not self.constraints(var, val, var2, val2)
        return count_if(conflict, self.neighbors[var])

def backtracking(csp):
    update(csp)
    return recursive_backtracking({}, csp)

def recursive_backtracking(assignment, csp):
    if len(csp.var) == len(assignment):
        return assignment
    var = select_unassigned_variable(assignment, csp)

    for val in order_domain_values(var, assignment, csp):
        if csp.nconflicts(var, val, assignment) == 0:
            csp.assign(var, val, assignment)
            result = recursive_backtracking(assignment, csp)
            if result is not None:
                return result
            csp.unassign(var, assignment)
    return None


def select_unassigned_variable(assignment, csp):
    for v in csp.var:
        if v not in assignment:
            return v

def order_domain_values(var, assignment, csp):
    domain = csp.domains[var][:]
    while domain:
        yield domain[0]
        domain = domain[1:]

def count_if(fun, seq):
    f = lambda count, x: count + (fun(x))
    return reduce(f, seq, 0)

class UniversalDict:
    def __init__(self, val):
        self.value = val
    def __getitem__(self, key):
        return self.value


# our constraint a!=b
def different_values_constraint(A, a, B, b):
    return a != b

def update(x, **entries):
    if isinstance(x, dict):
        x.update(entries)
    else:
        x.__dict__.update(entries)
    return x


vars = ['a', 'b', 'c']
domains = UniversalDict([1, 2, 3])
neighbors = {'a': ['b'], 'b': ['a', 'c'], 'c': ['b']}
result=backtracking(CSP(vars, domains, different_values_constraint, neighbors))
print(result)


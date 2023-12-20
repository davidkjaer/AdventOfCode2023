import re
from typing import List
from dataclasses import dataclass
from functools import reduce
import copy

@dataclass
class Rule:
    var: str
    op: str
    limit: int
    goal: str

@dataclass
class WorkFlow:
    name: str
    rules: List[Rule]
    final: str

workflows = {}
def parseWorkFlow(arg: str):
    match = re.match("(.+){(.+)}", arg)
    name, r = match.group(1), match.group(2)
    #print(name, r)
    individualRules = r.split(",")
    wf = WorkFlow(name, [], individualRules[-1])
    for rule in individualRules[:-1]:
        match = re.match(r"([xmas])([<>])(\d+):(.+)", rule)
        wf.rules.append(Rule(match.group(1), match.group(2), int(match.group(3)), match.group(4)))
    workflows[name] = wf


def evaluateWf(wf: WorkFlow, product: dict):
    #print(wf)
    for rule in wf.rules:
        match rule.op:
            case "<":
                if product[rule.var] < rule.limit:
                    #print("Returning goal <:", rule.goal)
                    return rule.goal
            case ">":
                if product[rule.var] > rule.limit:
                    #print("Returning goal >:", rule.goal)
                    return rule.goal

    #print("Returning final:", wf.final)
    return wf.final

def evaluate(product):
    currentWf = workflows["in"]
    while True:
        match evaluateWf(currentWf, product):
            case 'R':
                return False
            case 'A':
                return True
            case nextWfName:
                currentWf = workflows[nextWfName]

@dataclass
class Range:
    min: int
    max: int

def countNumberOfValid():
    allSums = 0

    def rec(wf: WorkFlow, ranges):
        nonlocal allSums
        if any(r.max < r.min for r in ranges.values()):
            return 0
        match wf.name:
            case "A":
                allSums += reduce(lambda x, y: x * y, [r.max - r.min + 1 for r in ranges.values()], 1)
            case "R":
                return 0
            case _:
                result = 0
                for rule in wf.rules:
                    match rule.op:
                        case "<":
                            oldMax = ranges[rule.var].max
                            ranges[rule.var].max = min(ranges[rule.var].max, rule.limit - 1)
                            rec(workflows[rule.goal], copy.deepcopy(ranges))
                            ranges[rule.var].max = oldMax
                            ranges[rule.var].min = max(ranges[rule.var].min, rule.limit)
                        case ">":
                            oldMin = ranges[rule.var].min
                            ranges[rule.var].min = max(ranges[rule.var].min, rule.limit + 1)
                            rec(workflows[rule.goal], copy.deepcopy(ranges))
                            ranges[rule.var].min = oldMin
                            ranges[rule.var].max = min(ranges[rule.var].max, rule.limit)
                rec(workflows[wf.final], copy.deepcopy(ranges))

    rec(workflows["in"], {"x": Range(1, 4000), "m": Range(1, 4000), "a": Range(1, 4000), "s": Range(1, 4000)})
    return allSums


with open("input.txt", "r") as input:
    while True:
        line = input.readline().strip()
        if not line:
            break
        parseWorkFlow(line)
    workflows["A"] = WorkFlow("A", [], "A")
    workflows["R"] = WorkFlow("R", [], "R")
    print(countNumberOfValid())

    result = 0
    while True:
        line = input.readline().strip()
        if not line:
            break
        product = line[1:-1]
        params = product.split(",")
        pmap = {}
        for p in params:
            match = re.match(r"([xmas])=(\d+)", p)
            pmap[match.group(1)] = int(match.group(2))
        if evaluate(pmap):
            result += sum(pmap.values())

    print(result)
#include <stdio.h>
#include "solution.h"

#define MAX(a, b) (a > b ? a : b)

#define CUBE_INIT(color)                                                       \
  group_t color(unsigned int value) {                                          \
    group_t cube = {.color = value};                                           \
    return cube;                                                               \
  }

CUBE_INIT(red)
CUBE_INIT(green)
CUBE_INIT(blue)

group_t groupUnion(group_t left, group_t right) {
  group_t u = {.red = MAX(left.red, right.red),
               .green = MAX(left.green, right.green),
               .blue = MAX(left.blue, right.blue)};
  return u;
}

unsigned int groupPower(group_t group) {
  return group.red * group.green * group.blue;
}


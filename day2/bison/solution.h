#ifndef AOC_DAY2_H_
#define AOC_DAY2_H_

typedef struct group {
  unsigned int red;
  unsigned int green;
  unsigned int blue;
} group_t;

group_t red(unsigned int value);
group_t green(unsigned int value);
group_t blue(unsigned int value);

group_t groupUnion(group_t left, group_t right);

unsigned int groupPower(group_t group);

#endif // AOC_DAY2_H_

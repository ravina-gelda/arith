load harness

@test "substraction-1" {
  check '2 - 3 * 4' '-10'
}

@test "substraction-2" {
  check '0 * 1 - -2' '2'
}

@test "substraction-3" {
  check '3 * 8 - 9 * 10' '-66'
}

@test "substraction-4" {
  check '3 - 3' '0'
}

@test "substraction-5" {
  check '3 + 4 - -5 - -10' '22'
}

@test "substraction-6" {
  check '-1 - -1 - -1 * 10' '10'
}

@test "substraction-7" {
  check '-1 - -1 - -1 * -10' '-10'
}

@test "substraction-8" {
  check '0 * 0 - 0 + -0' '0'
}

@test "substraction-9" {
  check '-2 * -4 * -2 + 3 * 8 - 10 - 2 + 3 * 4' '8'
}

@test "substraction-10" {
  check '-1 - -0 * 8' '-1'
}

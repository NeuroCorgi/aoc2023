import Foundation

let nums_p1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
  .enumerated()

let nums_p2
  = ["1","2","3","4","5","6","7","8","9",
     "_",
     "one","two","three","four","five",
     "six","seven","eight","nine"]
  .enumerated()

func first(of col: EnumeratedSequence<[String]>, in str: any StringProtocol) -> Int {
    return col
      .reduce((digit: 0, index: str.endIndex)) { (acc, el)  in
          if let index = str.range(of: el.element, options: .literal, range: nil, locale: nil)?.lowerBound,
             index <= acc.index {
              return ((el.offset + 1) % 10, index)
          }
          return acc
      }
      .digit
}

func last(of col: EnumeratedSequence<[String]>, in str: any StringProtocol) -> Int {
    return col
      .reduce((digit: 0, index: str.startIndex)) { (acc, el)  in
          if let index = str.range(of: el.element, options: .backwards, range: nil, locale: nil)?.lowerBound,
             index >= acc.index {
              return ((el.offset + 1) % 10, index)
          }
          return acc
      }
      .digit
}

let data = try String(contentsOfFile: CommandLine.arguments[1])
  .split(separator: "\n")

let part1 = data
  .map { first(of: nums_p1, in: $0) * 10 + last(of: nums_p1, in: $0) }
  .reduce(0, +)
print("Part 1: \(part1)")

let part2 = data
  .map {elem in first(of: nums_p2, in: elem) * 10 + last(of: nums_p2, in: elem)}
  .reduce(0, +)
print("Part 2: \(part2)")

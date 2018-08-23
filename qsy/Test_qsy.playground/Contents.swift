//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

let nums0 = [1,3,6]
let nums1 = [Int](repeating: 0, count: 6)
var nums_mutable = [34,64,9,23]
nums_mutable.append(77)
nums_mutable.sort()
nums_mutable.sort(by:>)
let anotherNums = Array(nums_mutable[0..<nums_mutable.count - 1])

// 实现栈
class Stack {
    var stack : [AnyObject]
    var isEmpty : Bool {
        return stack.isEmpty
    }
    var peak : AnyObject? {
        return stack.last
    }
    init() {
        stack = [AnyObject]()
    }
    func push(object: AnyObject){
        stack.append(object)
    }
    func pop() -> AnyObject? {
        if(!isEmpty) {
            return stack.removeLast()
        } else {
            return nil
        }
    }
}

let primeNums : Set = [3,23,6]
let oddNums : Set = [34,64,29]





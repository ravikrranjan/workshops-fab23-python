class Stack {
	push(value) {
		this.head = { value, next: this.head };
	}
	pop() {
		let value;
		return ([value, this.head] = [this.head.value, this.head.next]), value;
	}
}

const s = new Stack();

s.push(3);
s.push(5);
console.log(s);

console.log(s.pop());
console.log(s.pop());
// console.log(s.pop());

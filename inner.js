const print = (arg) => console.log(arg);

const arrowFun = () => {
	print("D", this.prototype);
};

function fatFun() {
	print("D", this.prototype);
}

print(arrowFun.prototype);

print(fatFun.prototype);

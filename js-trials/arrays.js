
const items = ['a', 'b', 'c'];

/** 1. printIndices */
function printIndices(items2) {
	for (const i in items2) {
    console.log(items2[i], i);
  } 
}


/** 2. everyOtherItem */
function everyOtherItem(items3) {
  const result = [];
  for (const i in items3) {
    if (i % 2 == 0) {
      result.push(items3[i]);
    }
  }
  console.log(result);
}


console.log(printIndices(items))

console.log(everyOtherItem(items))



/** 3. smallestNItems */
function smallestNItems(items4) {
  
}

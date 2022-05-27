exports.anagramsFor = function(word, listOfWords) {
    let resArr = [];
    for(let checking of listOfWords)
    if (word.toLowerCase().split('').sort().join('')
     === checking.toLowerCase().split('').sort().join('')){
         resArr.push(checking)
     }
     return resArr;
};

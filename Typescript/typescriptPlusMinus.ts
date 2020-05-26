function plusMinus(arr) {
    let positives:number = 0, negatives:number = 0, zeros:number = 0;
    const len = arr.length || 0;
     
    if (len > 0 && len <= 100) {
         arr.map((elem, key) => {
              if (elem > 0) {
                   positives++;
              } else if (elem < 0) {
                   negatives++; 
              } else {
                   zeros++;
              }
                 
              return elem; 
         }); 
         console.log((positives / len) || 0);
         console.log((negatives / len) || 0);
         console.log((zeros / len) || 0);      
    
    } 
  

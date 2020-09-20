let textGroupings = document.querySelectorAll('.text-grouping');
let centerGroupings = document.querySelectorAll('.center');
let chunks = document.querySelectorAll('.chunk');

textGroupings = Array.from(textGroupings);
centerGroupings = Array.from(centerGroupings);
chunks = Array.from(chunks)

textGroupings.forEach((textGrouping, index) => {
    if(index % 2 == 1){
        
    }
});

// //fade in
// document.addEventListener('scroll', e =>{
//     console.log(window.scrollY);
//     console.log(window.innerHeight)

//     textGroupings.forEach((textGroup, index) => {
//         let rect = textGroup.getBoundingClientRect();
//         if(rect.top > window.scrollY && rect.bottom < window.scrollY + window.innerHeight){
//             if(index%2 == 1){
//                 textGroup.classList.add('fadeFromRight');
//             }
//             else{
//                 textGroup.classList.add('fadeFromLeft');
//             }
//         }
//         else{
//             textGroup.style.opacity = 0;
//             if(textGroup.classList.contains('fadeFromRight')){
//                 textGroup.classList.remove('fadeFromRight')
//             }
//             if(textGroup.classList.contains('fadeFromLeft')){
//                 textGroup.classList.remove('fadeFromLeft');
//             }
//         }
//     })
// })





//searching
let searchBar = document.getElementById('search-bar');
searchBar.addEventListener('keyup' , e => {
    console.log('triggered');
    if(searchBar.value !== ""){
        searchMessage = searchBar.value.toLowerCase();
        console.log(searchMessage);
        chunks.forEach(chunk => {
            let targetPhrase = chunk.children[0].children[0].textContent.toLowerCase();

            if(targetPhrase.indexOf(searchMessage) === -1){
                chunk.style.display = 'none';
            }
            else{
                chunk.style.display = 'flex';
            }
        })

    }
    else{
        chunks.forEach(chunk => {
            chunk.style.display = 'flex';
        })
    }   
})
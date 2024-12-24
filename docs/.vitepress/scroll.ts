import createHyphenator from "hyphen";
import patterns from "./id";


export async function useScroll (){
  function getElementsWithNoChildren (target, document) {
    let candidates;

    if (target && typeof target.querySelectorAll === 'function') {
      candidates = target.querySelectorAll('*');
    }
    else if (target && typeof target.length === 'number') {
      candidates = target;
    }
    else {
      candidates = document.querySelectorAll('*');
    }

    return Array.from(candidates).filter((elem: any) => {
      return elem.children.length === 0;
    });
  };

  const findEl = async (hash: string , x = 100, document ) => {
    let el = document.querySelector(hash)
    let searchTexts = hash.split('#').join('').split('-')
    let searchText = searchTexts[0]
    let elems = getElementsWithNoChildren(document.querySelector('.vp-doc'), document)
    let matchingElementArr = Array.from(elems).filter((v:any) => v.textContent.includes(searchText));
    if(matchingElementArr.length){
      return matchingElementArr[0]
    }
    if(!!el){
      return el
    }
    if (x > 50) {
      return ''
    }

    return setTimeout(() => { findEl(hash, ++x || 1, document) }, 300)
  }
  
  
  function wrapKeywordWithHTML(keyword: string){
    return `<mark style="bg-yellow-300">${keyword}</mark>`
  }

  
  // const hyphenate = createHyphenator(patterns, { async: true });
  const hyphenateHTML = createHyphenator(patterns, { async: true, html: true });
  // const hyphenateHTMLSync = createHyphenator(patterns, { html: true });
  // const hyphenateSync = createHyphenator(patterns);
  
  if(window.location.hash.length){
    const hash = window.location.hash
    const searchTexts = [...new Set([...hash.replace(/[^A-Za-z]/ig, ' ').split(' ')])].filter( w => w.length).filter(w => ['dan'].indexOf(w) === -1)
    const els = [
      ...document.querySelectorAll('.vp-doc p'),
      ...document.querySelectorAll('.vp-doc ol'),
      ...document.querySelectorAll('.vp-doc ul'),
    ]
    if(els.length) {
      for (let el of els) {
        for(const searchText of searchTexts){
          let a = new RegExp(`(?<=>[^>]*)(${searchText})(?=[^>]*<)`, 'gi')
          let b = el.innerHTML.match(a)
          if(!b){
            a = new RegExp(`${searchText}`, 'gi')
            b = el.innerHTML.match(a)
          }
          if(b?.length){
            el.innerHTML = el.innerHTML.replace(a, wrapKeywordWithHTML)
          }
        }
      }
    } 
  }

  const hypEls = [
    ...Array.from(document.querySelectorAll('.vp-doc p')),
    ...Array.from(document.querySelectorAll('.vp-doc h1')),
    ...Array.from(document.querySelectorAll('.vp-doc h2')),
    ...Array.from(document.querySelectorAll('.vp-doc h3')),
    ...Array.from(document.querySelectorAll('.vp-doc h4')),
    ...Array.from(document.querySelectorAll('.vp-doc ol')),
    ...Array.from(document.querySelectorAll('.vp-doc ul')),
  ]
  for(let hypEl of hypEls){
    const asyncHTML = <Promise<any>>hyphenateHTML(hypEl.innerHTML, { 
      minWordLength: 3 
    })
    asyncHTML.then( result =>{
      hypEl.innerHTML = result
    })
  }

  if(window.location.hash.length){
    const elto = await findEl(window.location.hash, 100, document) as HTMLElement
    if ('scrollBehavior' in document.documentElement.style) {
      window.scrollTo({ top: elto.offsetTop - 20, behavior: 'smooth' })
    } else {
      window.scrollTo(0, elto.offsetTop)
    }
  } else {
    window.scrollTo(0, 0)
  }
}
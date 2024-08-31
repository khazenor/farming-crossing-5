global.generateBookContent = (author, title, rows) => {
  let outString = 'minecraft:written_book['
  outString += 'written_book_content={'
  outString += `author:"${author}",`
  outString += 'pages:['
  outString += global.getPagesContent(rows)
  outString += '],' // pages
  outString += 'resolved:1b,'
  outString += `title:{raw:"${title}"}`
  outString += '}' // written_book_content
  outString += ']' // minecraft:written_book
  
  return outString
}

global.getPagesContent = (rows) => {
  let pagesContent = ''
  let pageArrays = global.getPageArrays(rows)
  for (let i = 0; i<pageArrays.length; i++) {
    let pageArray = pageArrays[i]
    pagesContent += global.getPageContent(pageArray)
    if (i < pageArrays.length - 1) {
      pagesContent += ','
    }
  }
  return pagesContent
}

global.getPageContent = (pageArray) => {
  let pageContent = `{raw:'"`
  
  for (let row of pageArray) {
    pageContent += global.cleanString(row)
    pageContent += `\n`
  }

  pageContent += `"'}`
  return pageContent
}

global.getPageArrays = (rows) => {
  let numRowInPage = 14
  let pages = [[]]
  for (let row of rows) {
    if (pages[pages.length - 1].length === numRowInPage) {
      pages.push([row])
    } else {
      pages[pages.length - 1].push(row)
    }
  }
  return pages
}
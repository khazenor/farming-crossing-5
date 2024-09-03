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
  let pages = [[]]
  let curPageIdx = 0
  for (let row of rows) {
    let curPage = pages[curPageIdx]
    if (global.canPageAddRow(curPage, row)) {
      curPage.push(row)
    } else {
      pages.push([row])
      curPageIdx ++
    }
  }
  return pages
}

global.canPageAddRow = (page, row) => {
  let rowLimit = 14
  let curRows = global.getNumRowInPage(page)
  let numRowsNeeded = global.getNumRowsNeeded(row)
  let rowsLeft = rowLimit - curRows
  return rowsLeft >= numRowsNeeded
}

global.getNumRowInPage = (page) => {
  let numRowsInPage = 0
  for (let row of page) {
    numRowsInPage += global.getNumRowsNeeded(row)
  }
  return numRowsInPage
}

global.getNumRowsNeeded = (row) => {
  let colLimit = 19
  if (row.length > colLimit) {
    return 2
  } else {
    return 1
  }
}
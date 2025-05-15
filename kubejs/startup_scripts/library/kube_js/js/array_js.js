const ArrayJs = {
  safeAccess (array, index, defaultVal) {
    if (index >= array.length) {
      if (defaultVal) {
        return defaultVal
      } else {
        return null
      }
    }
    return array[index]
  }
}
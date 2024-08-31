const checkAreYouSure = (player) => {
  let timeLimit = 10
  let areYouSureTime = parseFloat(global.genStrFromObj(player.persistentData.areYouSureTime))
  let curTime = getCurTime()
  if (areYouSureTime && (curTime - areYouSureTime < timeLimit)) {
    return true
  } else {
    player.persistentData.areYouSureTime = `${curTime}`
    return false
  }
}

const getCurTime = () => {
  return Math.floor(new Date().getTime() / 1000)
}

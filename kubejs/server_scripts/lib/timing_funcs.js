// priority: 1

let timeLogByPlayer = {}

const checkAreYouSure = (player) => {
  return checkAreYouSureLike(player, 'checkAreYouSure', 10)
}

const checkAreYouSureLike = (player, activityId, timeLimit) => {
  if (lastActivityLessThan(player, activityId, timeLimit)) {
    clearActivity(player, activityId)
    return true
  } else {
    return false
  }
}

const lastActivityLessThan = (player, activityId, time) => {
  let timeSince = timeSinceLastActivity(player, activityId)
  return timeSince > 0 && timeSince <= time
}

const lastActivityMoreThan = (player, activityId, time) => {
  let timeSince = timeSinceLastActivity(player, activityId)
  if (timeSince === -1) {
    return true // returns true for first time
  }

  return timeSince >= time
}

const timeSinceLastActivity = (player, activityId) => {
  let curTime = getCurTime()
  if (hasLastActivity(player, activityId)) {
    let lastTime = getLastActivityTime(player, activityId)
    logActivity(player, activityId)
    return curTime - lastTime
  } else {
    logActivity(player, activityId)
    return -1
  }
}

const logActivity = (player, activityId) => {
  setActivity(player, activityId, getCurTime())
}

const clearActivity = (player, activityId) => {
  setActivity(player, activityId, null)
}

const setActivity = (player, activityId, value) => {
  let playerName = player.name.getString()
  if (!(playerName in timeLogByPlayer)) {
    let addObj = {}
    addObj[activityId] = value
    timeLogByPlayer[playerName] = addObj
  } else {
    timeLogByPlayer[playerName][activityId] = value
  }
}

const getLastActivityTime = (player, activityId) => {
  let playerName = player.name.getString()
  return timeLogByPlayer[playerName][activityId]
}

const hasLastActivity = (player, activityId) => {
  let playerName = player.name.getString()
  if (!timeLogByPlayer[playerName]) {
    return false
  } else if (!timeLogByPlayer[playerName][activityId]) {
    return false
  } else {
    return true
  }
}

const getCurTime = () => {
  return Number(new Date().getTime() / 1000)
}

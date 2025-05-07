// from cyb0124 of KubeJS discord
// https://discord.com/channels/303440391124942858/1279263174167756815/1279263212784717844

/////////////////////////
// Menu Implementation //
/////////////////////////

let MenuState = function(type, player, pageIndicatorLabel, pageIndicatorClickCallback) {
  this.player = player;
  this.type = type;
  this.page = 0;
  this.pageIndicatorLabel = pageIndicatorLabel
  this.pageIndicatorClickCallback = pageIndicatorClickCallback
  player.openChestGUI(type.title, 6, (gui) => this.gui = gui);
  this.showPage();
};

MenuState.prototype.showPage = function() {
  for (let slot of this.type.pages[this.page]) {
    let btn = this.gui.getSlot(slot.x, slot.y);
    btn.setItem(Item.of(slot.item).withName(slot.label));
    for (let event of ['LeftClicked', 'RightClicked', 'MiddleClicked', 'Swapped', 'Thrown', 'ShiftLeftClicked', 'ShiftRightClicked', 'DoubleClicked']) {
      let handler = slot['on' + event];
      handler && btn['set' + event](() => handler(this.player));
    }
  }
  let disabledItem = "minecraft:barrier";
  let enabledItemRight = CollectGuiConst.id.rightArrowId;
  let enabledItemLeft = CollectGuiConst.id.leftArrowId;
  let enabled = this.page > 0;
  this.gui.button(0, 5,
    enabled ? enabledItemLeft : disabledItem,
    Text.translate('menu.prevPage'),
    () => this.prevPage()
  );
  enabled = this.page < this.type.pages.length - 1;
  this.gui.button(8, 5,
    enabled ? enabledItemRight : disabledItem,
    Text.translate('menu.nextPage'),
    () => this.nextPage()
  );
  let pageNum = this.page + 1;
  
  if (this.pageIndicatorClickCallback) {
    this.gui.button(4, 5, 
      Item.of("minecraft:paper", pageNum),
      this.pageIndicatorLabel,
      () => {this.pageIndicatorClickCallback()}
    )
  } else {
    this.gui.button(4, 5,
      Item.of("minecraft:paper", pageNum),
      Text.translate('menu.pageNum', StrHelper.cleanFloor(pageNum)),
      () => {});
  }
};

MenuState.prototype.clearPage = function() {
  for (let slot of this.type.pages[this.page]) {
    let btn = this.gui.getSlot(slot.x, slot.y);
    btn.setItem("minecraft:air");
    btn.resetClickHandlers();
  }
};

MenuState.prototype.prevPage = function() {
  if (this.page <= 0) return;
  this.clearPage();
  --this.page;
  this.showPage();
};

MenuState.prototype.nextPage = function() {
  if (this.page >= this.type.pages.length - 1) return;
  this.clearPage();
  ++this.page;
  this.showPage();
};

let MenuType = function(title, pageIndicatorLabel, pageIndicatorClickCallback) {
  this.title = title;
  this.pages = [];
  this.pageIndicatorLabel = pageIndicatorLabel
  this.pageIndicatorClickCallback = pageIndicatorClickCallback
};

MenuType.prototype.getPage = function(i) {
  if (this.pages[i] === undefined)
    this.pages[i] = [];
  return this.pages[i];
};

MenuType.prototype.addSlot = function(slot) {
  this.getPage(slot.page).push(slot);
};

MenuType.prototype.show = function(player) {
  if (this.pageIndicatorClickCallback) {
    new MenuState(this, player, this.pageIndicatorLabel, this.pageIndicatorClickCallback);
  } else {
    new MenuState(this, player);
  }
};

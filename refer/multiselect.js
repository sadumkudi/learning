/* ---------------------- type#1 ----------------------------------- */

var multiSel = function(params) {
  this.sel = params.sel;
  this.box = params.box;
  this.data = {};
  //this.options ={};
  console.log('btn..', params.btn);
  for (var i = 0; i < params.btn.length; i++) {
    params.btn[i].addEventListener("click", this, false);
  }
}

multiSel.prototype = {
  handleEvent: function(event) {
    var action = $(event.target).attr('data-ms');
    console.log('target:', action);
    if (action == 'add') {
      this.data.v = this.sel.val();
      this.data.t = this.sel.find('option:selected').text();
      if (this.data.v == 'default') {
        return;
      }
      this._addToBox();
      this._hideOption();
    } else if (action == 'remove') {
      this.target = $(event.target).parent();
      this._removeFromBox();
      this._showOption();
    } else {
      console.log('Ooooopsie!');
    }
  },

  _addToBox: function() {
    var spn = $('.sltd-box span.sltd-item.sample').clone(true, true);
    spn.html(this.data.t + spn.html());
    spn.removeClass('sample');
    spn.data('id', this.data.v);
    spn[0].addEventListener("click", this, false); //true clone did not carry the event. maybe cause of the js binding?
    this.box.append(spn);
  },

  _hideOption: function() {
    this.sel.find('option[value="' + this.data.v + '"]').hide();
    this.sel.val('default'); //reset to default
  },
  _showOption: function() {
    this.sel.find('option[value="' + this.data.v + '"]').show();
    this.sel.val('default'); //hmm...
  },
  _removeFromBox: function() {
    this.data.v = this.target.data('id');
    this.target.remove();
  }
};

$(document).ready(function() {
  var params = {
    sel: $('#sel'),
    box: $('#box'),
    btn: $('.ms-actn')
  };
  var ms = new multiSel(params);
});

/* -------------------------- type#2 -------------------------------------- */
var quickMultiSel = function(params) {
  this.bl = params.bl;
  this.br = params.br
  this.data = {};
  for (var i = 0; i < params.btn.length; i++) {
    params.btn[i].addEventListener("click", this, false);
  }
}

quickMultiSel.prototype = {
  handleEvent: function(event) {
    var action = $(event.target).attr('data-qml');
    console.log('target:', action);
    if (action == 'left') {
      this.data.from = this.br;
      this.data.to = this.bl;
      this._shiftItems();
    } else if (action == 'right') {
      this.data.from = this.bl;
      this.data.to = this.br;
      this._shiftItems();
    } else if (action == 'item') {
      $(event.target).toggleClass('locked');
    } else {
      console.log('Ooooopsie!');
    }
  },
  _shiftItems: function() {
    this.data.from.find('.locked').appendTo(this.data.to).removeClass('locked');
  }

};

$(document).ready(function() {
  var params = {
    bl: $('#l_box'),
    br: $('#r_box'),
    btn: $('#set2 .ctrl-box,#set2 .open-item')
  };
  var ms = new quickMultiSel(params);
});

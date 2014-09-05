window.jQuery = window.$ = require 'jquery'
require 'jquery-nestable'
_ = require 'underscore'
Backbone = require 'backbone'


module.exports = class CMSNamedMenuAdmin extends Backbone.View

    initialize: (@options) ->

      _.each @options.cmsPages, (page, i) =>
        $div = $('<div class="dd-handle" />').text(page.title)

        $('<li class="dd-item" />').attr('data-id', i).append($div).appendTo @$el.find('.available-pages ol')

      @$el.find('.available-pages').nestable
        group: 1
        expandBtnHTML: '<span class="toggle" data-action="expand">+</span>'
        collapseBtnHTML: '<span class="toggle" data-action="collapse">-</span>'

      @$el.find('.menu-pages').nestable
        group: 1

      @$el.find('aside').trigger 'mousemove'

      @$el.css 'min-height', @$el.height()












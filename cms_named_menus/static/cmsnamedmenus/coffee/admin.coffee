window.jQuery = window.$ = require 'jquery'
require 'jquery-nestable'
_ = require 'underscore'
Backbone = require 'backbone'


module.exports = class CMSNamedMenuAdmin extends Backbone.View

    nestableOptions:
        group: 1
        expandBtnHTML: '<span class="toggle" data-action="expand">+</span>'
        collapseBtnHTML: '<span class="toggle" data-action="collapse">-</span>'

    itemTemplate: _.template('<li class="dd-item" \
                                  data-id="<%= id %>" \
                                  data-title="<%= title %>"> \
                                  <div class="dd-handle"><%= title %></div> \
                              </li>')

    events:
      'change .menu-pages': 'updateJSON'

    initialize: (@options) ->

      $availablePagesList = @createNestedList @options.availablePages

      @$el.find('.available-pages').append $availablePagesList

      $menuPagesList = @createNestedList @options.menuPages

      @$el.find('.menu-pages').append $menuPagesList

      @$el.find('.available-pages, .menu-pages').nestable @nestableOptions

      @$el.find('aside').trigger 'mousemove'

      @$el.css 'min-height', @$el.height()

    createNestedList: (pages) ->

      if _.isNull(pages) or pages.length is 0
        return $('<div class="dd-empty"></div>');

      $ol = $('<ol />')

      _.each pages, (page, i) =>

        $node = @createNode page

        $node.appendTo $ol

      return $ol


    createNode: (data) ->

      $node = $ @itemTemplate(data)

      return $node unless data.children

      $ol = $('<ol />')

      _.each data.children, (node, i) =>

        $child = $ @createNode node

        $child.appendTo $ol

      $node.append $ol

      return $node


    updateJSON: (e) =>

      data = $(e.currentTarget).nestable('serialize')


      $('#id_pages').val JSON.stringify(data)














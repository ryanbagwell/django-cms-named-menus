path = require 'path'
shelljs = require 'shelljs'

module.exports = (grunt) ->
  _ = grunt.util._


  # Used instead of "ext" to accommodate filenames with dots. Lots of
  # talk all over GitHub, including here: https://github.com/gruntjs/grunt/pull/750
  coffeeRename = (dest, src) -> path.join dest, "#{ src.replace /\.(lit)?coffee$/, '.js' }"

  # Project configuration.
  grunt.initConfig
    pkg: grunt.file.readJSON 'package.json'

    less:
      compile:
        files: [
          expand: true
          cwd: './cms_named_menus/static/cmsnamedmenus/less'
          src: ['admin.less']
          dest: './cms_named_menus/static/cmsnamedmenus/css'
          ext: '.css'
        ]


    watch:
      options:
        spawn: true
      coffee:
        options:
          cwd: './cms_named_menus/static/cmsnamedmenus/coffee'
        files: ['**/*.coffee']
        tasks: ['webpack']
      less:
        options:
          cwd: './cms_named_menus/static/cmsnamedmenus/less'
        files: ['**/*.less']
        tasks: ['less']

    uglify:
      options:
          mangle: false
      files:
        expand: true
        flatten: false
        cwd: './cms_named_menus/static/cmsnamedmenus/coffee'
        src: '**/*.js'
        dest: './cms_named_menus/static/eventtracking/js'

    webpack:
      all:
        cache: true
        devtool: 'sourcemap'
        entry:
          "admin": "admin"
        output:
          path: "cms_named_menus/static/cmsnamedmenus/js"
          filename: "[name].js"
          library: 'App'
        resolve:
          extensions: ['.coffee', '.js', '']
          modulesDirectories: [
            'node_modules'
            './cms_named_menus/static/cmsnamedmenus/coffee/'
          ]
          alias:
            'jquery-nestable':'jquery-nestable/jquery.nestable'
        module:
          loaders: [
            {test: /jquery\.js$/, loader: 'expose?$!expose?jQuery'}
            {test: /\.coffee$/, loader: 'coffee'}
          ]
        stats:
          colors: true
          modules: true
          reasons: true
        watch: false
        keepalive: false


  # Load grunt plugins
  grunt.loadNpmTasks 'grunt-contrib-coffee'
  grunt.loadNpmTasks 'grunt-contrib-watch'
  grunt.loadNpmTasks 'grunt-contrib-uglify'
  grunt.loadNpmTasks 'grunt-contrib-less'
  grunt.loadNpmTasks 'grunt-webpack'


  # Define tasks.
  grunt.registerTask 'build', ['less', 'webpack:all']


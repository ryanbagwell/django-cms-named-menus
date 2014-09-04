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


    coffee:
      compile:
        options:
          sourceMap: true
        files: [
          expand: true
          cwd: './eventtracking/static/eventtracking/coffee'
          src: ['**/*.{coffee,litcoffee}']
          dest: './eventtracking/static/eventtracking/js'
          rename: coffeeRename
        ]

    watch:
      options:
        spawn: true
      coffeeMain:
        options:
          cwd: './eventtracking/static/eventtracking/coffee'
        files: ['**/*.coffee']
        tasks: ['coffee:compile']


    uglify:
      options:
          mangle: false
      files:
        expand: true
        flatten: false
        cwd: './eventtracking/static/eventtracking/js'
        src: '**/*.js'
        dest: './eventtracking/static/eventtracking/js'



  # Load grunt plugins
  grunt.loadNpmTasks 'grunt-contrib-coffee'
  grunt.loadNpmTasks 'grunt-contrib-watch'
  grunt.loadNpmTasks 'grunt-contrib-uglify'


  # Define tasks.
  grunt.registerTask 'build', ['coffee', 'uglify']
  grunt.registerTask 'default', ['watch']
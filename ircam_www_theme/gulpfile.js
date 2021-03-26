var gulp = require('gulp'),
    rimraf = require('rimraf'),
    sass = require('gulp-sass'),
    sassMagicImporter = require ('node-sass-magic-importer'),
    postcss = require ('gulp-postcss'),
    uglify = require('gulp-uglify'),
    concat = require('gulp-concat'),
    ignore = require('gulp-ignore'),
    cssnano = require('gulp-cssnano'),
    rename = require('gulp-rename'),
    browserSync = require('browser-sync').create(),
    runSequence = require('run-sequence'),
    imagemin = require('gulp-imagemin')
    favicons = require('gulp-favicons'),
    gutil = require('gulp-util'),
    copy = require('gulp-copy'),
    plumber = require('gulp-plumber'),
    autoprefixer = require('autoprefixer'),
    browserify = require('gulp-browserify'),
    util = require('util'),
    sourcemaps = require('gulp-sourcemaps');

var srcFolder = 'static/src/',
    destFolder = 'static/'

gulp.task('copy-assets-img', function() {
    gulp.src([srcFolder + 'assets/img/**/*'])
        .pipe(gulp.dest(destFolder + 'img'));
});

gulp.task("favicons", function () {
    return gulp.src(srcFolder + "assets/favicon/favicon.png")
        .pipe(favicons({
            background: "#ffffff",
            path: "/favicons/",
            replace: true,
            icons: {
                android: false,              // Create Android homescreen icon. `boolean`
                appleIcon: true,            // Create Apple touch icons. `boolean`
                appleStartup: false,         // Create Apple startup images. `boolean`
                coast: false,                // Create Opera Coast icon. `boolean`
                favicons: true,             // Create regular favicons. `boolean`
                firefox: false,              // Create Firefox OS icons. `boolean`
                opengraph: false,            // Create Facebook OpenGraph image. `boolean`
                twitter: false,              // Create Twitter Summary Card image. `boolean`
                windows: false,              // Create Windows 8 tile icons. `boolean`
                yandex: false                // Create Yandex browser icon. `boolean`
            }
        }))
        .on("error", gutil.log)
        .pipe(gulp.dest(destFolder + '/img/favicons/'));
});

gulp.task('main-js', function() {
    return gulp.src(srcFolder + 'js/index.js')
        .pipe(plumber({
            errorHandler: function (error) {
                console.log(error.message);
                this.emit('end');
            }})
        )
        .pipe(browserify({
		  insertGlobals : true,
		  debug : false
		}))
        .pipe(rename('index.min.js'))
        .pipe(sourcemaps.init())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(destFolder + 'js'))
        .pipe(browserSync.stream());
});

gulp.task('main-css', function() {
    return gulp.src(srcFolder + 'sass/*.scss')
    .pipe(plumber())
    .pipe(sourcemaps.init())
    .pipe(sass({
      includePaths: ['node_modules', srcFolder + 'sass'],
      precision: 10,
      importer: sassMagicImporter({
        disableImportOnce: true
      })
    })).on('error', util.log.bind(util, 'Sass Error'))
    .pipe(postcss([
      autoprefixer()
    ]))
    .pipe(rename({suffix: '.min'}))
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(destFolder + 'css'))
    .pipe(browserSync.stream());
});

gulp.task('cssmin', function() {
    return gulp.src(destFolder + 'css/**/*.css')
        .pipe(sourcemaps.init())
        .pipe(cssnano())
        .on("error", gutil.log)
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(destFolder + 'css/'))
        .pipe(browserSync.stream());
});

gulp.task('jsmin', function() {
    return gulp.src(destFolder + 'js/**/*.js')
        .pipe(sourcemaps.init())
        .pipe(uglify({'mangle': false}))
        .on("error", gutil.log)
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(destFolder + 'js/'))
        .pipe(browserSync.stream());
});

gulp.task('imagemin', function() {
	return gulp.src(destFolder + 'img/**/*')
		.pipe(imagemin({
			progressive: true,
            optimizationLevel: 3
		}))
        .on("error", gutil.log)
		.pipe(gulp.dest(destFolder + 'img'));
});

gulp.task('clean', function(cb) {
    rimraf('.tmp', cb);
});

gulp.task('serve', ['clean'], function () {

    browserSync.init({
        proxy: "http://localhost:9020/"
    });

    gulp.watch(srcFolder + 'assets/img/**/*', ['copy-assets-img']).on('change', browserSync.reload);
	gulp.watch(srcFolder + 'js/**/*.js', ['main-js']);
	gulp.watch(srcFolder + 'sass/**/*.scss', ['main-css']);

});

gulp.task('default', ['main-js', 'main-css', 'copy-assets-img', 'serve']);
gulp.task('build', ['main-js', 'main-css', 'copy-assets-img'], function() {
    runSequence(['cssmin', 'jsmin', 'imagemin', 'favicons', 'clean']);
});

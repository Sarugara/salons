
var app = angular.module('app', ['ngAnimate', 'ngRoute', 'controllers', 'constant']);




app.config(function($routeProvider,  $locationProvider){
/*	$locationProvider.html5Mode(true);*/

	$routeProvider
	.when('/salons', {
		templateUrl: '../static/salons.html',
		controller: 'SalonsCtrl'
	})
	.when('/actionssalons', {
		templateUrl: '../static/actionssalons.html',
		controller: 'ActionsSalonsCtrl'
	})
	.when('/workssalons', {
		templateUrl: '../static/workssalons.html',
		controller: 'WorksSalonsCtrl'
	})
	.when('/allsalons', {
		templateUrl: '../static/allsalons.html',
		controller: 'AllSalonsCtrl'
	})
	.when('/clinic', {
		templateUrl: '../static/clinic.html'
	})
});

app.directive('extends', function($animate) {
        return {
            link: function (scope, elem, attrs) {
            	scope.addExtends = function(){
            		var self = angular.element(elem);
                    $animate.addClass(self, 'in-body-right-div-active', function () {
                    });
            	}
            	scope.removeExtends = function(){
            		var self = angular.element(elem);
                    self.removeClass('in-body-right-div-active');
            	}
            	
            }
        };
});

app.directive('changetype', ['$animate',
    function ($animate) {
        return {
            link: function (scope, elem, attrs) {
            	scope.cl = function(){
            		var self = angular.element(elem);
                    $animate.addClass(self, 'bottomline', function () {
                        
                    });
            	}
/*                elem.on('click', function () {
                    var self = angular.element(this);
                    $animate.addClass(self, 'bottomline', function () {
                        self.removeClass('bottomline');
                    });
                });*/
            }
        };
}]);




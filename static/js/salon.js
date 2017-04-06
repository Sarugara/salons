
var salon = angular.module('salon', [ 'ngRoute', 'ngAnimate']);


salon.config(['$routeProvider', '$locationProvider', function($routeProvider,  $locationProvider){
/*	$locationProvider.html5Mode(true);*/

	$routeProvider
	.when('/salon/:salonId', {
		templateUrl: 'salonprofile.html',
		controller: 'SalonsCtrl'
	})
}]);


salon.directive('changetype', ['$animate',
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


salon.controller('divCtrl', function($scope){
    $scope.showMenu = false;
    var toogle = true;
    $scope.menuShowHide = function(){   
        alert("Hi");
        $scope.showMenu = toogle;           
        toogle=!toogle;
        if($scope.showMenu){
            $scope.addExtends();
        }else{
            $scope.removeExtends();
        }
        
    }
});



salon.controller('SalonsCtrl', function($scope){

    $scope.salon = [
        {
            name: "salonle",
            desc: "Информативное описание компаний и их слоган",
            adress: "Точный и понятный адресс, 34",
            logo: "img/back.jpg"
        }
    ]

});
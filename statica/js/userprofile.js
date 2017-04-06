
var app = angular.module('app', ['ngAnimate', 'ngRoute', 'controllers']);




app.config(function($routeProvider,  $locationProvider){
/*	$locationProvider.html5Mode(true);*/

	$routeProvider
	.when('/user/:userId', {
		templateUrl: 'users.html',
		controller: 'ProfileCtrl'
	})
    .when('/login', {
        templateUrl: 'login.html',
        controller: 'LoginCtrl'  
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

app.controller('ProfileCtrl', ['$scope', '$routeParams', function($scope, $routeParams){
        
        $scope.addBusy = true;

        $scope.addBusyFunc = function(){
            
                $scope.addBusy=!$scope.addBusy;
            
        }

        $scope.editUser = true;

        $scope.editUserFunc = function(){
            
                $scope.editUser=!$scope.editUser;
            
        }


        var user =
        [
            {id:0,
            name:'Yeskendir',
            group: 'User',
            desc: 'В поисках удивительного преображения жизни удивительного преображения жизни удивительного преображения жизни'},
            {id:1,
            name:'Salgara',
            group: 'Admin',
            desc: 'Очень хороший сайт. inst: /trololo'},
        ];

        for(var i=0; i<user.length; i++){
            if($routeParams.userId==user[i].id){
                $scope.user = user[i];    
            }
        }




        $scope.bestsalons = [
        {
            name: "Apple",
            desc: "Информативное описание компаний и их слоган",
            adress: "Точный и понятный адресс, 34",
            logo: "img/back.jpg"
        },
        {
            name: "Samsung",
            desc: "Информативное описание компаний и их слоган",
            adress: "Точный и понятный адресс, 34",
            logo: "img/back2.jpg"
        },
        {
            name: "Nissan",
            desc: "Информативное описание компаний и их слоган",
            adress: "Точный и понятный адресс, 34 Apple",
            logo: "img/back3.jpg"
        },
        {
            name: "Tesla",
            desc: "Информативное описание компаний и их слоган",
            adress: "Точный и понятный адресс, 34",
            logo: "img/back.jpg"
        },
        {
            name: "Sony",
            desc: "Информативное описание компаний и их слоган",
            adress: "Точный и понятный адресс, 34 Volva",
            logo: "img/back.jpg"
        },
        {
            name: "Honda",
            desc: "Информативное описание компаний и их слоган",
            adress: "Точный и понятный адресс, 34",
            logo: "img/back2.jpg"
        },
        {
            name: "Google",
            desc: "Информативное описание компаний и их слоган",
            adress: "Точный и понятный адресс, 34",
            logo: "img/back3.jpg"
        },
        {
            name: "SpaceX",
            desc: "Информативное описание компаний и их слоган",
            adress: "Точный и понятный адресс, 34",
            logo: "img/back.jpg"
        },
        {
            name: "Toyota",
            desc: "Информативное описание компаний и их слоган",
            adress: "Точный и понятный адресс, 34",
            logo: "img/back.jpg"
        },
        {
            name: "Volva",
            desc: "Информативное описание компаний и их слоган",
            adress: "Точный и понятный адресс, 34",
            logo: "img/back2.jpg"
        },
        {
            name: "A7 Salon",
            desc: "Информативное описание компаний и их слоган",
            adress: "Точный и понятный адресс, 34",
            logo: "img/back3.jpg"
        },
        {
            name: "Unity",
            desc: "Информативное описание компаний и их слоган",
            adress: "Точный и понятный адресс, 34",
            logo: "img/back.jpg"
        }
    ]

        
}]);

app.controller('LoginCtrl', ['$scope', '$routeParams', function($scope, $routeParams){
        

        $scope.authShow = false;
        $scope.regShow = true;
        $scope.passShow = true;

        $scope.authShowFunc = function(){
            $scope.authShow = false;
            $scope.regShow = true;
            $scope.passShow = true;
        }


        $scope.regShowFunc = function(){
            $scope.authShow = true;
            $scope.regShow = false;
            $scope.passShow = true;
        }

        $scope.passShowFunc = function(){
            $scope.authShow = true;
            $scope.regShow = true;
            $scope.passShow = false;
        }


        
}]);


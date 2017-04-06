var app = angular.module('controllers', ['ngAnimate', 'ngCookies']);

app.controller('divCtrl', function($scope, $http, $timeout, $cookies, $window){
	$scope.showMenu = false;
	var toogle = true;
	$scope.menuShowHide = function(){		
		$scope.showMenu = toogle;			
		toogle=!toogle;
		if($scope.showMenu){
			$scope.addExtends();
		}else{
			$scope.removeExtends();
		}
		
	}


});


app.controller('ChangeTypeCtrl', function($scope){
	$scope.cssclass = "typechange1";
});




app.controller('SalonsCtrl', function($scope, $http){

	$http.get('http://localhost:8000/salons/api/all/?format=json')
                .then(function successCallback(response) {
                    $scope.bestsalons = response.data;
                  }, function errorCallback(response) {
                    console.log('Error respond');
                  });

});

app.controller('ActionsSalonsCtrl', function($scope){
	
	$scope.actionssalons = [
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

});
app.controller('WorksSalonsCtrl', function($scope){
	$scope.workssalons = [
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
});
app.controller('AllSalonsCtrl', function($scope){
	$scope.allsalons = [
		{
			name: "A7 Salon",
			desc: "Информативное описание компаний и их слоган",
			adress: "Точный и понятный адресс, 34",
			logo: "img/back3.jpg"
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
			name: "Unity",
			desc: "Информативное описание компаний и их слоган",
			adress: "Точный и понятный адресс, 34",
			logo: "img/back.jpg"
		}
		
	]
});



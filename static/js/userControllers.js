var app = angular.module('controllers', ['ngAnimate']);

app.controller('divCtrl', function($scope){
	$scope.showMenu = true;
	var toogle = false;
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




app.controller('SalonsCtrl', function($scope){

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



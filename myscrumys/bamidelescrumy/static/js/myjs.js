var scrumy=angular.module('scrumy',['ngRoute']);


scrumy.controller('ctrl',function($scope,$routeParams,$http){
    $http.get('/scrumyusers/?format=json').then(function(response){
        $scope.data=response.data;
    });

    $http.get('/scrumygoals/?format=json').then(function(response){
        $scope.task=response.data;
    });

    $http.get('/goalstatus/?format=json').then(function(response){
        $scope.status=response.data;
    });

$scope.role=['Owner','Developer','Quality Analyst','Admin'];
    $scope.addUser=function(){
        $http.post('/scrumyusers',{
                name:$scope.name,
                email:$scope.email,
                username:$scope.username,
                password:$scope.password,
                role:$scope.role
        }).success(function(data,status,headers,config){
            console.log('successfully inserted the data');
        });
        $scope.name='';
        $scope.email='';
        $scope.username='';
        $scope.password='';
        $scope.role='';
    };

    
    
});
// scrumy.controller('addCtrl',function($scope){
//    $http.post({
//        method:'POST',
//        url:"/scrumyusers",
//        data:{}
//    })
// });
scrumy.config(function($routeProvider){
    $routeProvider
    .when('/',{
        templateUrl:"/static/templates/inde.html"
    })
    .when('/addtask',{
        templateUrl:"/static/templates/add_tasks.html",
        controller:"ctrl"
    })
    .when('/adduser',{
        templateUrl:"/static/templates/add_users.html",
    });
});

scrumy.config(['$httpProvider',function($httpProvider){
    $httpProvider.defaults.xsrfCookieName='csrftoken';
    $httpProvider.defaults.xsrfHeaderName='X-CSRFToken';
}]);
function validatePass(pass1,pass2) {
    var p1 = document.getElementById(pass1).value;
    var p2 = document.getElementById(pass2).value;
    if(p1 != p2) {
        document.getElementById("passError").innerHTML="Passwords do not match!";
    }
    else {
        document.getElementById("passError").innerHTML="";
    }
    return pass == confirm;
}

var myApp = angular.module('myApp',[]);

myApp.service('dataService', function($http) {
delete $http.defaults.headers.common['X-Requested-With'];
this.getData = function(callbackFunc) {
    username = document.getElementById('username').value;
    $http({
        method: 'GET',
        url: 'http://localhost:8000/usernameexist',
        params: 'username=' + username
     }).success(function(data){
        // With the data succesfully returned, call our callback
        callbackFunc(data);
    }).error(function(){
        alert("error");
    });
 }
});
myApp.controller('myCtrl', function($scope, dataService) {
    $scope.data = null;
    dataService.getData(function(dataResponse) {
        if(dataResponse == 1) {
            $scope.data = 'Username Unavailable';
        }
        else  {
            $scope.data = '';
        }

    });
});
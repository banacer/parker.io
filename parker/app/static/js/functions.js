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
var myApp = angular.module('customersApp', []);

    myApp.factory('dataService', ['$http', function ($http) {
        var serviceBase = '/api/dataservice/',
            dataFactory = {};

        dataFactory.checkUniqueValue = function (value) {
            return $http.get(serviceBase + 'checkUnique/?username=' + escape(value)).then(
                function (results) {
                    return results.data;
                });
        };

        return dataFactory;

}]);
myApp.directive('wcUnique', ['dataService', function (dataService) {
    return {
        restrict: 'A',
        require: 'ngModel',
        link: function (scope, element, attrs, ngModel) {
        }
    }
}]);

myApp.directive('wcUnique', ['dataService', function (dataService) {
    return {
        restrict: 'A',
        require: 'ngModel',
        link: function (scope, element, attrs, ngModel) {
            element.bind('blur', function (e) {
                if (!ngModel || !element.val()) return;
                var currentValue = element.val();
                dataService.checkUniqueValue(currentValue)
                    .then(function (unique) {
                        if (currentValue == element.val()) {
                             console.log('unique = '+unique);
                             if(unique == 1) {
                                document.getElementById("usernameTakenMessage").innerHTML = "That username is taken, please try another"
                             }
                             else {
                                document.getElementById("usernameTakenMessage").innerHTML = ""
                             }
                             ngModel.$unique = unique
                             scope.$broadcast('show-errors-check-validity');
                        }
                    });
            });
        }
    }
}]);
import {Actions} from 'flummox';
import $ from 'jquery';
import {getCookie} from '../utils';


export default class AuthActions extends Actions {
    login(username, password) {
        $.ajax({
            url:'api/token-auth/',
            method: 'POST',
            data: {
                username: username,
                password: password
            }
        }).done(function(data) {
            console.info('success');
            console.info(data);
            return data;
        }).fail(function() {
            console.error('error');
        });
    }

    logout() {

    }

    register(username, email, password) {

    }

    checkUsername(username) {

    }

    checkEmail(email) {

    }
}

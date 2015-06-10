import {Store} from 'flummox';
import {NOT_CONNECTED} from '../constants';

export default class AuthStore extends Store {
    constructor(flux) {
        super();

        const authIds = flux.getActionIds('auth');

        this.register(authIds.loadUser, this.handleLoadUser);
        this.register(authIds.login, this.handleLogin);
        this.register(authIds.logout, this.handleLogout);

        this.state = {
            token: null,
            username: null,
            state: NOT_CONNECTED
        };
    }

    handleLoadUser(data) {
        this.setState({
            token: data.token,
            username: data.username,
            state: data.state
        });
    }

    handleLogin(data) {
        this.setState({
            token: data.token,
            username: data.username,
            state: data.state
        });
    }

    handleLogout() {
        this.setState({
            token: null,
            username: null,
            state: NOT_CONNECTED
        });
    }
}

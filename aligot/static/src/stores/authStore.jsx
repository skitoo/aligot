import {Store} from 'flummox';



export default class AuthStore extends Store {
    constructor(flux) {
        super();

        const authIds = flux.getActionIds('auth');

        this.register(authIds.loadUser, this.handleLoadUser);
        this.register(authIds.login, this.handleLogin);
        this.register(authIds.logout, this.handleLogout);

        this.state = {
            token: null,
            username: null
        };
    }

    handleLoadUser(data) {
        this.setState({
            token: data.token,
            username: data.username
        });
    }

    handleLogin(data) {
        this.setState({
            token: data.token,
            username: data.username
        });
    }

    handleLogout() {
        this.setState({
            token: null,
            username: null
        });
    }
}

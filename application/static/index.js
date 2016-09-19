import React from 'react';
import ReactDOM from 'react-dom';
import Relay from 'react-relay';

import StreetList from './street-list';

Relay.injectNetworkLayer(
    new Relay.DefaultNetworkLayer('/relay/graphql/', {
        credentials: 'same-origin',
    })
);

class App extends React.Component {
    render() {
        return (
            <div>
                <h1>Streets</h1>
                <StreetList streets={ this.props.viewer.streets } />
            </div>
        );
    }
}

const RelayApp = Relay.createContainer(App, {
    fragments: {
        viewer: () => Relay.QL`
            fragment on Viewer {
                streets {
                    ${StreetList.getFragment('streets')}
                }
            }
        `,
    },
});

const Viewer = {
    queries: {
         viewer: () => Relay.QL`
             query { viewer }
         `,
     },
    params: {},
    name: 'Viewer',
};

ReactDOM.render(
    <Relay.RootContainer
        Component={ RelayApp }
        route={ Viewer }
    />,
    document.getElementById('application'),
);

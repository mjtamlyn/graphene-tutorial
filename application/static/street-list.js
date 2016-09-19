import React from 'react';
import Relay from 'react-relay';


class StreetList extends React.Component {
    render() {
        let streets = this.props.streets.map((street) => {
            return (<li key={ street.id }>
                <a>{ street.name }</a>
            </li>);
        });
        return (<ul>
            { streets }
        </ul>);
    }
};

export default Relay.createContainer(StreetList, {
    fragments: {
        streets: () => Relay.QL`
            fragment on StreetNode @relay(plural: true) {
                id
                name
            }
        `,
    },
});

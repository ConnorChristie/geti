// Copyright (C) 2022-2025 Intel Corporation
// LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE

import { screen } from '@testing-library/react';
import { userEvent } from '@testing-library/user-event';

import { LabelTreeGroupProps } from '../../../../../core/labels/label-tree-view.interface';
import { getMockedTreeGroup } from '../../../../../test-utils/mocked-items-factory/mocked-labels';
import { providersRender as render } from '../../../../../test-utils/required-providers-render';
import { checkTooltip, MORE_THAN_100_CHARS_NAME } from '../../../../../test-utils/utils';
import { GroupEditionMode } from './group-edition-mode.component';

describe('Group edition mode', () => {
    const saveMock = jest.fn();
    const mockedGroup = getMockedTreeGroup({ name: 'test' }) as LabelTreeGroupProps;

    it('check if group is limited to 100 chars in label edition', async () => {
        render(
            <GroupEditionMode
                flatListProjectItems={[]}
                save={saveMock}
                item={{ ...mockedGroup, name: '' }}
                savedItem={mockedGroup}
                newTree={true}
                setValidationError={jest.fn()}
                validationErrors={{}}
            />
        );

        const groupField = screen.getByPlaceholderText('Label group name');
        await userEvent.click(groupField);
        await userEvent.paste(MORE_THAN_100_CHARS_NAME);

        expect(saveMock).toHaveBeenLastCalledWith(
            expect.objectContaining({ name: MORE_THAN_100_CHARS_NAME.substring(0, 100) })
        );
    });

    it('Check if Multiple Selection tooltip is properly shown on text', async () => {
        render(
            <GroupEditionMode
                flatListProjectItems={[]}
                save={jest.fn()}
                item={mockedGroup}
                savedItem={mockedGroup}
                setValidationError={jest.fn()}
                validationErrors={{}}
                newTree={true}
            />
        );

        await checkTooltip(
            screen.getByText('Multiple selection'),
            'Off - Only one label from such group can be applied to an image/frame. ' +
                'On - Multiple labels from such group can be applied to an image/frame.'
        );
    });
});

// Copyright (C) 2022-2025 Intel Corporation
// LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE

import { ComponentProps, MutableRefObject, ReactNode } from 'react';

import { ActionButton, Button, CustomPopover, Divider, Flex, Popover, Text } from '@geti/ui';
import { Close } from '@geti/ui/icons';
import { isFunction } from 'lodash-es';

import { openNewTab } from '../../../../utils';

import classes from './fux-notification.module.scss';

interface CustomPopoverProps extends Omit<ComponentProps<typeof Popover>, 'triggerRef' | 'children'> {
    docUrl?: string;
    children: ReactNode;
    triggerRef: MutableRefObject<null>;
    onClose?: () => void;
}

export const FuxNotification = ({ docUrl, placement, triggerRef, state, onClose, children }: CustomPopoverProps) => {
    return (
        <CustomPopover
            ref={triggerRef}
            hideArrow={false}
            placement={placement}
            state={state}
            UNSAFE_className={classes.container}
            isKeyboardDismissDisabled
        >
            <Flex direction={'row'} gap={'size-200'} alignItems={'center'}>
                <Text order={1}>{children}</Text>

                {docUrl && (
                    <Button
                        order={2}
                        variant='primary'
                        UNSAFE_style={{ border: 'none' }}
                        onPress={() => openNewTab(docUrl)}
                    >
                        Learn more
                    </Button>
                )}

                <Divider order={3} orientation='vertical' size='S' UNSAFE_className={classes.divider} />

                <ActionButton
                    isQuiet
                    order={4}
                    onPress={() => {
                        state.close();
                        isFunction(onClose) && onClose();
                    }}
                    aria-label={'close first user experience notification'}
                    UNSAFE_className={classes.close}
                >
                    <Close />
                </ActionButton>
            </Flex>
        </CustomPopover>
    );
};

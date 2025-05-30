// Copyright (C) 2022-2025 Intel Corporation
// LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE

import { screen } from '@testing-library/react';
import { userEvent } from '@testing-library/user-event';

import { getMockedQuota } from '../../../../test-utils/mocked-items-factory/mocked-quota';
import { providersRender as render } from '../../../../test-utils/required-providers-render';
import { EditServiceLimitDialog } from './edit-service-limit-dialog.component';

describe('EditServiceLimitDialog', () => {
    it('does not allow the limit value to be greater than quota max limit', async () => {
        const quota = getMockedQuota({ maxLimit: 20, limit: 19 });

        render(<EditServiceLimitDialog quota={quota} onSave={jest.fn()} isOpen onOpenChange={jest.fn()} />);

        expect(
            screen.getByRole('textbox', {
                name: new RegExp(`${quota.serviceName} - ${quota.quotaName}`, 'i'),
            })
        ).toHaveValue('19');

        await userEvent.click(screen.getByRole('button', { name: /Increase/ }));

        expect(
            screen.getByRole('textbox', {
                name: new RegExp(`${quota.serviceName} - ${quota.quotaName}`, 'i'),
            })
        ).toHaveValue('20');

        await userEvent.click(screen.getByRole('button', { name: /Increase/ }));

        expect(
            screen.getByRole('textbox', {
                name: new RegExp(`${quota.serviceName} - ${quota.quotaName}`, 'i'),
            })
        ).toHaveValue('20');

        expect(screen.getByRole('button', { name: /Increase/ })).toHaveAttribute('aria-disabled', 'true');
    });

    it('does not allow the limit value to be lower than min service limit', async () => {
        const quota = getMockedQuota({ limit: 2 });

        render(<EditServiceLimitDialog quota={quota} onSave={jest.fn()} isOpen onOpenChange={jest.fn()} />);

        expect(
            screen.getByRole('textbox', {
                name: new RegExp(`${quota.serviceName} - ${quota.quotaName}`, 'i'),
            })
        ).toHaveValue('2');

        await userEvent.click(screen.getByRole('button', { name: /Decrease/ }));

        expect(
            screen.getByRole('textbox', {
                name: new RegExp(`${quota.serviceName} - ${quota.quotaName}`, 'i'),
            })
        ).toHaveValue('1');

        await userEvent.click(screen.getByRole('button', { name: /Decrease/ }));

        expect(
            screen.getByRole('textbox', {
                name: new RegExp(`${quota.serviceName} - ${quota.quotaName}`, 'i'),
            })
        ).toHaveValue('1');

        expect(screen.getByRole('button', { name: /Decrease/ })).toHaveAttribute('aria-disabled', 'true');
    });

    it('submits on save click', async () => {
        const quota = getMockedQuota({ maxLimit: 20, limit: 19 });

        const handleSave = jest.fn();

        render(<EditServiceLimitDialog quota={quota} onSave={handleSave} isOpen onOpenChange={jest.fn()} />);

        await userEvent.click(screen.getByRole('button', { name: /Increase/ }));

        await userEvent.click(screen.getByRole('button', { name: /Save/ }));

        expect(handleSave).toHaveBeenCalledWith({ ...quota, limit: 20 });
    });

    it('save button is disabled when limit is equal to quota limit', async () => {
        const quota = getMockedQuota({ maxLimit: 20, limit: 19 });

        render(<EditServiceLimitDialog quota={quota} onSave={jest.fn()} isOpen onOpenChange={jest.fn()} />);

        expect(
            screen.getByRole('textbox', {
                name: new RegExp(`${quota.serviceName} - ${quota.quotaName}`, 'i'),
            })
        ).toHaveValue('19');
        expect(screen.getByRole('button', { name: /Save/ })).toBeDisabled();
    });
});

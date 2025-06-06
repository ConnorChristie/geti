// Copyright (C) 2022-2025 Intel Corporation
// LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE

import { RangeValue } from '@geti/ui';
import { CalendarDate } from '@internationalized/date';
import { screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

import { providersRender as render } from '../../../../../test-utils/required-providers-render';
import { DateRangePickerSmall } from './date-range-picker-small.component';

describe('DateRangePickerSmall Component', () => {
    const MOCKED_TODAY = new CalendarDate(2025, 4, 30);

    const INITIAL_DATES: RangeValue<CalendarDate> = {
        start: MOCKED_TODAY.subtract({ months: 1 }),
        end: MOCKED_TODAY,
    };

    const mockOnChange = jest.fn();

    const renderComponent = () =>
        render(
            <DateRangePickerSmall
                value={INITIAL_DATES}
                onChange={mockOnChange}
                hasManualEdition={true}
                headerContent='Select Date Range'
            />
        );

    afterEach(() => {
        userEvent.keyboard('{escape}');
    });

    it('should open the date range dialog when the button is clicked', async () => {
        renderComponent();

        await userEvent.click(screen.getByRole('button', { name: 'Select date range' }));
        expect(await screen.findByRole('dialog')).toBeVisible();

        expect(screen.getByText('Select Date Range')).toBeInTheDocument();
        expect(await screen.findByRole('dialog')).toBeVisible();
    });

    it('should allow manual editing of the date range', async () => {
        renderComponent();

        const button = screen.getByRole('button', { name: 'Select date range' });
        expect(button).toBeInTheDocument();

        await userEvent.click(button);
        expect(await screen.findByRole('dialog')).toBeVisible();

        const march3rdButton = screen.getByRole('button', { name: 'Monday, March 3, 2025' });
        const march8thButton = screen.getByRole('button', { name: 'Saturday, March 8, 2025' });

        await userEvent.click(march3rdButton);
        await userEvent.click(march8thButton);

        expect(mockOnChange).toHaveBeenCalledWith(
            expect.objectContaining({
                end: expect.objectContaining({ day: 8, month: 3, year: 2025 }),
                start: expect.objectContaining({ day: 3, month: 3, year: 2025 }),
            })
        );
    });
});

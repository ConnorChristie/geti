// Copyright (C) 2022-2025 Intel Corporation
// LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE

import { Dispatch, SetStateAction, useCallback, useEffect, useMemo, useState } from 'react';

import { isEqual } from 'lodash-es';

import { useConfigParameters } from '../../../../../../core/configurable-parameters/hooks/use-config-parameters.hook';
import {
    ConfigurableParametersComponents,
    ConfigurableParametersTaskChain,
} from '../../../../../../core/configurable-parameters/services/configurable-parameters.interface';
import {
    getReconfigureParametersDTO,
    updateSelectedParameter,
} from '../../../../../../core/configurable-parameters/utils';
import { useProjectIdentifier } from '../../../../../../hooks/use-project-identifier/use-project-identifier';
import { getSelectedComponent } from '../../utils';

interface UseReconfigureParametersValue {
    isLoading: boolean;
    setIsQueryEnabled: Dispatch<SetStateAction<boolean>>;
    configParameters: ConfigurableParametersTaskChain[] | undefined;
    updateParameter<T extends string | boolean | number>(id: string, value: T): void;
    selectedComponentId: string | undefined;
    setSelectedComponentId: Dispatch<SetStateAction<string | undefined>>;
    selectedComponent: ConfigurableParametersComponents | undefined;
    reconfigure: (closeDialog: () => void) => void;
    isReconfigureButtonDisabled: boolean;
    isReconfiguring: boolean;
}

export const useReconfigureParametersValue = (): UseReconfigureParametersValue => {
    const projectIdentifier = useProjectIdentifier();
    const [isQueryEnabled, setIsQueryEnabled] = useState<boolean>(false);
    const { useGetConfigParameters, reconfigureParametersMutation } = useConfigParameters(projectIdentifier);

    const { isLoading, data } = useGetConfigParameters(isQueryEnabled);
    const [selectedComponentId, setSelectedComponentId] = useState<string | undefined>(undefined);
    const [configParameters, setConfigParameters] = useState<ConfigurableParametersTaskChain[] | undefined>(data);

    const selectedComponent = useMemo(
        () => getSelectedComponent(configParameters, selectedComponentId),
        [selectedComponentId, configParameters]
    );
    const [isReconfigureButtonDisabled, setIsReconfigureButtonDisabled] = useState<boolean>(true);

    const updateParameter = useCallback(<T extends string | boolean | number>(id: string, value: T): void => {
        const ids = id.split('::');

        ids.length > 2 &&
            setConfigParameters((prevConfigParameters) => {
                if (prevConfigParameters) {
                    return updateSelectedParameter(prevConfigParameters, id, ids, value);
                }

                return prevConfigParameters;
            });
    }, []);

    const reconfigure = (closeDialog: () => void) => {
        if (configParameters) {
            setIsReconfigureButtonDisabled(true);
            reconfigureParametersMutation.mutate(getReconfigureParametersDTO(configParameters), {
                onSuccess: () => {
                    setConfigParameters(undefined);
                    closeDialog();
                },
            });
        }
    };

    useEffect(() => {
        if (data) {
            setConfigParameters(data);
            setSelectedComponentId(data.length ? data[0].components[0]?.id : undefined);
        }
    }, [data]);

    useEffect(() => {
        if (data && configParameters) {
            setIsReconfigureButtonDisabled(isEqual(data, configParameters));
        }
    }, [data, configParameters]);

    return {
        configParameters,
        isLoading,
        setIsQueryEnabled,
        updateParameter,
        selectedComponent,
        selectedComponentId,
        setSelectedComponentId,
        reconfigure,
        isReconfigureButtonDisabled,
        isReconfiguring: reconfigureParametersMutation.isPending,
    };
};

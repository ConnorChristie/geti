// Copyright (C) 2022-2025 Intel Corporation
// LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE

import { ConfigurableParametersComponentsBodyDTO } from '../../../../core/configurable-parameters/dtos/configurable-parameters.interface';
import {
    ConfigurableParametersComponents,
    ConfigurableParametersTaskChain,
} from '../../../../core/configurable-parameters/services/configurable-parameters.interface';
import { getComponentsDTO } from '../../../../core/configurable-parameters/utils';
import { ModelGroupsAlgorithmDetails, ModelsGroups } from '../../../../core/models/models.interface';
import { PerformanceCategory } from '../../../../core/supported-algorithms/dtos/supported-algorithms.interface';
import { TaskWithSupportedAlgorithms } from '../../../../core/supported-algorithms/supported-algorithms.interface';
import { hasEqualId } from '../../../../shared/utils';

export const getSelectedComponent = (
    configParameters: ConfigurableParametersTaskChain[] | undefined,
    selectedComponentId: string | undefined
): ConfigurableParametersComponents | undefined => {
    return configParameters?.map((config) => config.components.find(hasEqualId(selectedComponentId))).find(Boolean);
};

export const getTrainingConfigParametersDTO = ({
    components,
}: ConfigurableParametersTaskChain): { components: ConfigurableParametersComponentsBodyDTO[] } => {
    return {
        components: getComponentsDTO(components),
    };
};

export const addAlgorithmDetails =
    (tasksWithSupportedAlgorithms: TaskWithSupportedAlgorithms) =>
    (model: ModelsGroups): ModelGroupsAlgorithmDetails => {
        const match = tasksWithSupportedAlgorithms[model.taskId]?.find(({ name }) => name === model.groupName);

        return {
            ...model,
            isDefaultAlgorithm: match?.isDefaultAlgorithm ?? false,
            performanceCategory: match?.performanceCategory ?? PerformanceCategory.OTHER,
            complexity: match?.gigaflops ?? null,
        };
    };

// Code generated by mockery. DO NOT EDIT.

package frames

import (
	bytes "bytes"

	mock "github.com/stretchr/testify/mock"
)

// MockFrameReader is an autogenerated mock type for the FrameReader type
type MockFrameReader struct {
	mock.Mock
}

type MockFrameReader_Expecter struct {
	mock *mock.Mock
}

func (_m *MockFrameReader) EXPECT() *MockFrameReader_Expecter {
	return &MockFrameReader_Expecter{mock: &_m.Mock}
}

// ReadFrameToBuffer provides a mock function with given fields: path, frameNum
func (_m *MockFrameReader) ReadFrameToBuffer(path string, frameNum int) (*bytes.Buffer, error) {
	ret := _m.Called(path, frameNum)

	if len(ret) == 0 {
		panic("no return value specified for ReadFrameToBuffer")
	}

	var r0 *bytes.Buffer
	var r1 error
	if rf, ok := ret.Get(0).(func(string, int) (*bytes.Buffer, error)); ok {
		return rf(path, frameNum)
	}
	if rf, ok := ret.Get(0).(func(string, int) *bytes.Buffer); ok {
		r0 = rf(path, frameNum)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*bytes.Buffer)
		}
	}

	if rf, ok := ret.Get(1).(func(string, int) error); ok {
		r1 = rf(path, frameNum)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// MockFrameReader_ReadFrameToBuffer_Call is a *mock.Call that shadows Run/Return methods with type explicit version for method 'ReadFrameToBuffer'
type MockFrameReader_ReadFrameToBuffer_Call struct {
	*mock.Call
}

// ReadFrameToBuffer is a helper method to define mock.On call
//   - path string
//   - frameNum int
func (_e *MockFrameReader_Expecter) ReadFrameToBuffer(path interface{}, frameNum interface{}) *MockFrameReader_ReadFrameToBuffer_Call {
	return &MockFrameReader_ReadFrameToBuffer_Call{Call: _e.mock.On("ReadFrameToBuffer", path, frameNum)}
}

func (_c *MockFrameReader_ReadFrameToBuffer_Call) Run(run func(path string, frameNum int)) *MockFrameReader_ReadFrameToBuffer_Call {
	_c.Call.Run(func(args mock.Arguments) {
		run(args[0].(string), args[1].(int))
	})
	return _c
}

func (_c *MockFrameReader_ReadFrameToBuffer_Call) Return(_a0 *bytes.Buffer, _a1 error) *MockFrameReader_ReadFrameToBuffer_Call {
	_c.Call.Return(_a0, _a1)
	return _c
}

func (_c *MockFrameReader_ReadFrameToBuffer_Call) RunAndReturn(run func(string, int) (*bytes.Buffer, error)) *MockFrameReader_ReadFrameToBuffer_Call {
	_c.Call.Return(run)
	return _c
}

// ReadFrameToBufferFps provides a mock function with given fields: path, frameNum, fps
func (_m *MockFrameReader) ReadFrameToBufferFps(path string, frameNum int, fps float64) (*bytes.Buffer, error) {
	ret := _m.Called(path, frameNum, fps)

	if len(ret) == 0 {
		panic("no return value specified for ReadFrameToBufferFps")
	}

	var r0 *bytes.Buffer
	var r1 error
	if rf, ok := ret.Get(0).(func(string, int, float64) (*bytes.Buffer, error)); ok {
		return rf(path, frameNum, fps)
	}
	if rf, ok := ret.Get(0).(func(string, int, float64) *bytes.Buffer); ok {
		r0 = rf(path, frameNum, fps)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*bytes.Buffer)
		}
	}

	if rf, ok := ret.Get(1).(func(string, int, float64) error); ok {
		r1 = rf(path, frameNum, fps)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// MockFrameReader_ReadFrameToBufferFps_Call is a *mock.Call that shadows Run/Return methods with type explicit version for method 'ReadFrameToBufferFps'
type MockFrameReader_ReadFrameToBufferFps_Call struct {
	*mock.Call
}

// ReadFrameToBufferFps is a helper method to define mock.On call
//   - path string
//   - frameNum int
//   - fps float64
func (_e *MockFrameReader_Expecter) ReadFrameToBufferFps(path interface{}, frameNum interface{}, fps interface{}) *MockFrameReader_ReadFrameToBufferFps_Call {
	return &MockFrameReader_ReadFrameToBufferFps_Call{Call: _e.mock.On("ReadFrameToBufferFps", path, frameNum, fps)}
}

func (_c *MockFrameReader_ReadFrameToBufferFps_Call) Run(run func(path string, frameNum int, fps float64)) *MockFrameReader_ReadFrameToBufferFps_Call {
	_c.Call.Run(func(args mock.Arguments) {
		run(args[0].(string), args[1].(int), args[2].(float64))
	})
	return _c
}

func (_c *MockFrameReader_ReadFrameToBufferFps_Call) Return(_a0 *bytes.Buffer, _a1 error) *MockFrameReader_ReadFrameToBufferFps_Call {
	_c.Call.Return(_a0, _a1)
	return _c
}

func (_c *MockFrameReader_ReadFrameToBufferFps_Call) RunAndReturn(run func(string, int, float64) (*bytes.Buffer, error)) *MockFrameReader_ReadFrameToBufferFps_Call {
	_c.Call.Return(run)
	return _c
}

// NewMockFrameReader creates a new instance of MockFrameReader. It also registers a testing interface on the mock and a cleanup function to assert the mocks expectations.
// The first argument is typically a *testing.T value.
func NewMockFrameReader(t interface {
	mock.TestingT
	Cleanup(func())
}) *MockFrameReader {
	mock := &MockFrameReader{}
	mock.Mock.Test(t)

	t.Cleanup(func() { mock.AssertExpectations(t) })

	return mock
}
